package model.type;

import model.value.RefValue;
import model.value.Value;

public class RefType implements Type{
    Type inner;


    public RefType(Type inner) {
        this.inner = inner;
    }

    public Type getInner(){
        return this.inner;
    }

    @Override
    public boolean equals(Type anotherType) {
        if(anotherType instanceof RefType)
            return inner.equals(((RefType) anotherType).getInner());
        else
            return false;
    }

    @Override
    public Value defaultValue() {
        return new RefValue(0, inner);
    }

    @Override
    public Type deepCopy() {
        return new RefType(inner.deepCopy());
    }

    public String toString() { return "Ref(" +inner.toString()+")";}
}
